from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse
from rest_framework import status
from decouple import config
# ? Auth
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.utils.util.archivo_s3_class import ArchivoS3Class


# ? Clase



class ArchivoS3ApiViewSet(viewsets.ViewSet):
    # permission_classes = [AllowAny]

    # @action(detail=False, methods=['get'])
    # def read(self, request):
    #     resp = request.query_params.get
    #     orden = OrdenPedido.objects.filter(estado_pedido=resp('id_estado'), empresa_id=resp('id_empresa'),
    #                                        created_at__range=[resp('fecha_inicio'), (
    #                                            resp('fecha_fin'))]).all().order_by('created_at')
    #     ordenes = orden_pedido_serializer.OrdPedidoSerializer(orden, many=True).data

    #     return JsonResponse({'success': True, 'data': ordenes}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def upload(self, request):
        print('Iniciando.....')
        qp = request.query_params
        tipo = None

        if 'type' in qp.keys():
            tipo = qp.get('type')

        bucket = 'lsplus-files'
        folder = request.POST.get('folder')
        nombre = request.POST.get('nombre')

        data = []

        if request.FILES.get('files') is not None:
            for archivo in request.FILES.getlist('files'):

                result = ArchivoS3Class().upload(bucket=bucket, folder=folder, nombre=nombre, archivo=archivo,
                                                 tipo=tipo)
                if result is None: continue
                item = {
                    'bucket': result['bucket'],
                    'folder': result['folder'],
                    'nombre': result['nombre'],
                    'extension': result['extension'],
                    'uuid': result['uuid'],
                    'url': result['url']
                }
                data.append(item)
        return JsonResponse({'success': True,'message':'Se listo correctamente', 'data': data}, status=status.HTTP_200_OK)
