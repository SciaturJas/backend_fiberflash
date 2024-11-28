
from email.utils import formataddr

from apps.utils.util.send_function import EmailObject


def execute(params):
    # Send Email to student

    source_name = "FiberFlash Contacto"
    source = formataddr((source_name, "contacto@lsplus.pe"))
    curso_name=params['course_name']
    subject = f'BIENVENIDO/A - A TU NUEVO CURSO {curso_name} | SEÑAS PLUS'
    pass

    # html_content = get_html_bienvenida(params)
    # to = ['contacto@lsplus.pe']
    # email = EmailObject(subject=subject,
    #                     source=source,
    #                     to=to,
    #                     html_content=html_content,
    #                     path_file=None)
    # email.do_sendmail()