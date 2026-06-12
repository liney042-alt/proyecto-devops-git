# 1. Usar una imagen base ligera y oficial
FROM python:3.12-slim

# 2. Definir el directorio de trabajo seguro
WORKDIR /app

# 3. Copiar el archivo de la aplicación
COPY app.py .

# 4. Crear un usuario de sistema no privilegiado y dar permisos a las carpetas
RUN useradd -r -u 10001 appuser && \
    mkdir -p /data && \
    chown -R appuser:appuser /app /data

# 5. Cambiar al usuario no root para la ejecución
USER appuser

# 6. Informar el puerto que usa la aplicación
EXPOSE 8080

# 7. Agregar el Healthcheck para producción
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/health')"

# 8. Comando para iniciar la aplicación
CMD ["python", "app.py"]