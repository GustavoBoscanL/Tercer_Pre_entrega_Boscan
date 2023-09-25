# Tercera_pre_entrega_Boscan

## **Proyecto de Gestión de Datos**
Este proyecto es una aplicación web que utiliza herencia de HTML para gestionar datos de usuarios, empleados y precios del autolavado. El objetivo principal es proporcionar un sistema de gestión de datos robusto y fácil de usar que permita a los usuarios realizar varias operaciones, como agregar datos, buscar en la base de datos y visualizar información de manera eficiente.

## **Características Principales**
**-Herencia de HTML**: Este proyecto utiliza herencia de HTML para mantener un 
diseño coherente en toda la aplicación. La estructura de HTML se gestiona de manera centralizada para garantizar una interfaz de usuario uniforme.

**-Modelos de Datos**: Hemos definido tres clases principales en el directorio "models" que representan las entidades clave de nuestro sistema: Users, Employees y Washing_Prices. Cada una de estas clases modela los datos relacionados con su respectiva entidad y se utiliza para interactuar con la base de datos.

**-Formularios de Inserción**: Se han creado formularios distintos para cada una de las clases de modelos mencionadas anteriormente. Estos formularios permiten a los usuarios ingresar datos de manera sencilla y precisa, lo que facilita la administración de la información.

**-Búsqueda en la Base de Datos**: Hemos implementado una funcionalidad de búsqueda que permite a los usuarios buscar registros en la base de datos de manera eficiente. Esto ayuda a encontrar información específica rápidamente y mejora la experiencia del usuario.

# Configuración y Uso



1.   **Clona el Repositorio**: Para comenzar, clona este repositorio en tu máquina local utilizando el siguiente comando:


```
git clone https://github.com/tu-usuario/tu-proyecto.git

```


2.   **Configura el Entorno**: Asegúrate de tener todas las dependencias necesarias instaladas y configuradas en tu entorno de desarrollo. Puedes hacerlo ejecutando:



```
pip install -r requirements.txt

```



3.   **Ejecuta la Aplicación**: Inicia la aplicación ejecutando el siguiente comando:


```
python manage.py runserver

```



4.   Accede a la Aplicación: Abre tu navegador web y ve a la dirección http://localhost:8000 para acceder a la aplicación.


URLs y Rutas


*   /users/: Esta ruta te llevará a la sección de gestión de usuarios.
*   /employees/: Accede a la sección de gestión de empleados.
*   /washing_prices/: Explora y administra los precios.
*   /search/: Utiliza esta ruta para realizar búsquedas en la base de datos.
