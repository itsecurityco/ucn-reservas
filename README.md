# ucn-reservas

Para descargar el código fuente correr el comando `git clone`
```bash
git clone git@github.com:itsecurityco/ucn-reservas.git
cd ucn-reservas
```

Para actualizar la aplicación correr el comando `git pull`
```bash
git pull
```

Hacer una copia del archivo `.env-example` y cambiar las contraseñas por defecto.
```bash
cp .env-example .env
```

Correr `docker-compose` en una consola
``` bash
docker-compose up
```

En otra ventana hacer la migración de la base de datos
``` bash
docker-compose run web python manage.py migrate
```

Crear el superusuario
```bash
docker-compose run web python manage.py createsuperuser
```

Acceder desde el navegador al administrador `http://localhost:8000/admin/` y crear los usuarios y dispostivios.

Para detener los servicios correr `docker-compose down`
``` bash
docker-compose down
```
