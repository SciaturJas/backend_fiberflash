import boto3
import pathlib
import urllib.parse
import uuid
import logging
import os
from decouple import Csv, config
from botocore.exceptions import ClientError


s3 = boto3.client('s3', region_name=config('AWS_SES_REGION_NAME'), aws_access_key_id=config('AWS_ACCESS_KEY'),
                  aws_secret_access_key=config('AWS_SECRET_KEY'))


class ArchivoS3Class:

    def __init__(self) -> None:
        print('se inicio')
        return

    def upload(self, bucket: str, nombre: str, archivo, folder: str = '', is_public=True, tipo=None):

        content_type = archivo.content_type
        if tipo in ['jpeg', 'jpg', 'peg']:
            content_type = 'image/jpeg'  # Forzar el Content-Type para imágenes JPEG
        elif tipo == 'png':
            content_type = 'image/png'
        elif tipo == 'pdf':
            content_type = 'application/pdf'

        fold = folder.replace(' ', '+')
        fold = fold.replace(',', '%2C')


        _uuid = str(pathlib.Path(archivo.name).stem) + '-uuid-' + str(uuid.uuid4()) + str(
            pathlib.Path(archivo.name).suffix)
        extension: str = str(pathlib.Path(archivo.name).suffix).split(".")[-1]
        url = 'https://%s.s3.amazonaws.com/%s' % (bucket, folder + urllib.parse.quote(_uuid))

        if tipo in ['pdf','jpeg', 'jpg', 'png','peg']:

            s3.upload_fileobj(archivo, bucket, folder + _uuid, ExtraArgs={'ACL': 'public-read',
                                                                          'ContentType': 'application/pdf',
                                                                          'ContentDisposition': 'inline'})
        else:
            s3.upload_fileobj(archivo, bucket, folder + _uuid, ExtraArgs={'ACL': 'public-read'})

        det = {
            'bucket':bucket,
            'folder':folder,
            'nombre':nombre,
            'extension':extension,
            'uuid':_uuid,
            'url':url
        }
        return det


    def listar_archivo(self, _bucket_: str, _key_: str) -> list:
        archivos: list = []
        for key in s3.list_objects(Bucket=_bucket_)['Contents']:
            archivos.append(key['Key'])
        return archivos

    def encontrar_archivo(self, _bucket_: str, _key_: str) -> int:
        total = 0
        for archivo in s3.list_objects(Bucket=_bucket_)['Contents']:
            if archivo['Key'] == _key_:
                total += 1
        return total

    def subir_archivo(self, _bucket_: str, _archivo_, _dir_: str = '') -> dict:
        if _bucket_ is None: return False
        if _archivo_ is None: return False
        nombre: str = str(pathlib.Path(_archivo_.name).stem)
        sufijo: str = str(pathlib.Path(_archivo_.name).suffix)
        extension: str = sufijo.split(".")[-1]
        _uuid = '-' + str(uuid.uuid4())
        key = str(_dir_) + nombre + _uuid + sufijo

        s3.upload_fileobj(_archivo_, _bucket_, key, ExtraArgs={'ACL': 'public-read'})

        data = {
            'estado': True,
            'bucket': _bucket_,
            'dir': _dir_,
            'nombre': nombre,
            'sufijo': sufijo,
            'uuid': _uuid,
            'key': key,
            'extension': extension,
            'url': 'https://%s.s3.amazonaws.com/%s' % (_bucket_, urllib.parse.quote(key))
        }

        return data

    def actualizar_archivo(self, _bucket_: str, _key_: str, _archivo_) -> bool:
        if _bucket_ is None: return False
        if _key_ is None: return False
        if _archivo_ is None: return False
        # consultar
        resultado = s3.upload_fileobj(_archivo_, _bucket_, _archivo_.name)
        return True

    def eliminar_archivo(self, _bucket_: str, _key_: str) -> bool:
        if _bucket_ is None: return False
        if _key_ is None: return False
        find = self.encontrar_archivo(_bucket_, _key_)
        if find == 0:
            return False
        s3.delete_object(Bucket=_bucket_, Key=_key_)
        return True

    def upload_file(self, file_name, bucket, object_name=None, directory=None):

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = os.path.basename(file_name)

        directory_path = directory + '/' + object_name
        # Upload the file
        try:
            response = s3.upload_file(file_name, bucket, directory_path, ExtraArgs={'ACL': 'public-read',
                                                                                    'ContentType': 'application/pdf',
                                                                                    'ContentDisposition': 'inline'})

            _uuid = str(pathlib.Path(object_name).stem) + '-uuid-' + str(uuid.uuid4()) + str(
                pathlib.Path(object_name).suffix)

            url = 'https://%s.s3.amazonaws.com/%s' % (bucket, directory + '/' + object_name)

            return url
        except ClientError as e:
            logging.error(e)
            return False