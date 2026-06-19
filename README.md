# Proyecto DevOps con Git y GitHub

bloque de código directamente en el archivo:

```markdown
# Proyecto DevOps: Desarrollo, Contenedorización y Orquestación

## 👥 Integrantes del Proyecto
* **Liney Ricardo**
* **Thomas Isaza**
* **Durman Vanegas**
* **Steven Tobon**

## 🏢 Contexto Institucional
* **Programa de Formación:** Análisis y Desarrollo de Software – ADSO[cite: 1]
* **Código del Programa:** 228118[cite: 1]
* **Componente:** DevOps y Contenedores (Docker)[cite: 1]
* **Centro de Formación:** Centro de Tecnología de la Manufactura Avanzada – CTMA[cite: 1]
* **Instructor:** Wilson Castro Gil[cite: 1]

---

## 📝 Descripción del Proyecto
Este repositorio consolida el flujo de trabajo de un pipeline moderno de desarrollo bajo la filosofía DevOps. Integra desde la escritura de lógica básica en Python, pasando por la contenedorización segura y el manejo de secretos (Semana 8), hasta el despliegue automático, escalamiento y administración declarativa utilizando Kubernetes (Semana 9)[cite: 1].

---

## 🛠️ Requisitos del Entorno
Para ejecutar las actividades de este proyecto, asegúrate de tener instalado:
* **Git** para control de versiones.
* **Python 3.x** para la ejecución de scripts lógicos.
* **Docker Desktop** con la opción de Kubernetes habilitada.
* **Kubectl** como interfaz de línea de comandos para el clúster[cite: 1].

---

##  Guía Paso a Paso de Uso e Infraestructura

###  SECCIÓN 1: Contenedorización y Seguridad (Semana 8)
El objetivo de esta fase fue empaquetar la aplicación en un entorno aislado, estandarizado y proteger la información sensible del proyecto.

#### Paso 1: Código Fuente y Lógica Base
* Se desarrolló un script básico en Python (`src/app.py`) enfocado en la resolución de lógica de programación mediante código limpio y accesible.

#### Paso 2: Construcción de la Imagen (Dockerfile)
* Se creó un archivo `Dockerfile` en la raíz para definir las instrucciones de empaquetamiento (sistema operativo base, dependencias y comando de arranque).

#### Paso 3: Orquestación Local con Docker Compose
* Se configuró el archivo `compose.yml` para levantar y coordinar los servicios locales de manera automática sin comandos manuales extensos.
* Para ejecutar este entorno, se utiliza el comando:
```bash
  docker compose up -d

```

#### Paso 4: Gestión de Secretos y Seguridad de Git

* **Carpeta `secrets/`:** Se creó un directorio dedicado exclusivamente para almacenar de forma local contraseñas, variables de entorno (`.env`) o claves de bases de datos.
* **Filtro de exclusión (`.gitignore`):** Se configuró el archivo `.gitignore` incluyendo la regla estricta de ignorar la carpeta `secrets/` y archivos `.env`. Esto garantiza que los datos sensibles permanezcan únicamente en la máquina local de desarrollo y nunca se filtren al repositorio público de GitHub.

---

### SECCIÓN 2: Orquestación con Kubernetes (Semana 9)

El objetivo de esta fase fue desplegar la aplicación simulando un entorno de producción de alta disponibilidad, escalable y auto-reparable utilizando objetos declarativos.

#### Paso 1: Verificación del Entorno Local

Antes de interactuar con el clúster, se comprueba que el control remoto (`kubectl`) reconozca el motor de Docker Desktop:

```bash
kubectl version --client
kubectl cluster-info
kubectl get nodes

```

#### Paso 2: Creación de un Entorno Aislado (Namespace)

Para segmentar lógicamente el clúster y evitar conflictos con otros proyectos, se crea un espacio de nombres dedicado:

```bash
kubectl create namespace laboratorio-k8s
kubectl config set-context --current --namespace=laboratorio-k8s

```

#### Paso 3: Despliegue de la Aplicación (Deployment)

Se inicializa un objeto Deployment de forma imperativa utilizando una imagen pública de servidor web (`nginx`):

```bash
kubectl create deployment web-nginx --image=nginx

```

* Para auditar la correcta inicialización del Pod y del contenedor, se ejecuta:



```bash
  kubectl get deployments
  kubectl get pods

```

#### Paso 4: Creación del Punto de Acceso Estable (Service)

Dado que los Pods son efímeros y sus IPs cambian, se expone el Deployment a través de un Service de tipo *ClusterIP* para garantizar un canal de red estable:

```bash
kubectl expose deployment web-nginx --port=80 --type=ClusterIP

```

#### Paso 5: Redirección de Tráfico Local (Port-Forward)

Para auditar la aplicación desde el navegador del equipo de desarrollo, se genera un puente de red temporal hacia el servicio:

```bash
kubectl port-forward service/web-nginx 8080:80

```

* **Verificación:** Abre el navegador e ingresa a `http://localhost:8080`. Se desplegará la pantalla oficial de *"Welcome to nginx!"*. Para liberar la consola, presiona `Ctrl + C`.



#### Paso 6: Escalado de Infraestructura

Para responder a altas demandas de tráfico de usuarios, se aumenta la disponibilidad incrementando el número de instancias en paralelo con un único comando:

```bash
kubectl scale deployment/web-nginx --replicas=3

```

* Verifica las 3 copias corriendo simultáneamente con `kubectl get pods`.



#### Paso 7: Despliegue Declarativo (Infraestructura como Código)

Para estandarizar el proceso bajo prácticas DevOps profesionales, se diseñó el manifiesto declarativo `kubernetes/deployment-demo.yaml`. Para aplicarlo de forma masiva en el sistema se ejecuta:

```bash
kubectl apply -f kubernetes/deployment-demo.yaml

```

#### Paso 8: Ciclo de Limpieza de Recursos

Como buena práctica de administración para liberar memoria RAM y procesamiento al finalizar las pruebas de laboratorio, se remueve el namespace completo, lo que destruye de manera automática todos los objetos asociados:

```bash
kubectl delete namespace laboratorio-k8s

```

---

## 📂 Estructura del Repositorio

```text
proyecto-devops-git/
├── kubernetes/
│   └── deployment-demo.yaml     # Manifiesto declarativo de Kubernetes (Semana 9)
├── secrets/                     # Datos sensibles locales (Semana 8 - Excluido en Git)
├── src/
│   └── app.py                   # Script de lógica de programación en Python
├── .gitignore                   # Filtros de exclusión para Git (Protección de secretos)
├── Dockerfile                   # Configuración de empaquetamiento de imagen Docker
├── compose.yml                  # Orquestador multi-contenedor local de Docker
└── README.md                    # Documentación general del proyecto (Este archivo)

```

---

Este repositorio forma parte de las evidencias de producto del portafolio formativo para el componente DevOps de ADSO - SENA.

```

```
