# Análisis Farmacocinético de Sunitinib en Ratones

Este proyecto tiene como objetivo comparar modelos farmacocinéticos mono-compartimental y bi-compartimental aplicados al fármaco Sunitinib en ratones.

## Modelos Evaluados

- **Modelo Mono-Compartimental**  
- **Modelo Bi-Compartimental**

## Métricas Calculadas

- **SSR (Suma de los Cuadrados del Residuo)**  
- **AIC (Criterio de Información de Akaike)**  

Estas métricas se utilizan para evaluar la calidad del ajuste de cada modelo a los datos experimentales.

## Lenguaje y Herramientas

- Python  
- Bibliotecas: NumPy, SciPy, Matplotlib, entre otras.

## Configuración de Uso

Recomendamos configurar un entorno virtual primero:

```bash
python -m venv venv
source venv/bin/activate  # o `venv\Scripts\activate` en Windows
```

Luego instala el backend en modo editable:

```bash
pip install -e .
```