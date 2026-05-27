Análisis de Ventas Comerciales – TUP 2026
Cátedra: Organización Empresarial
Institución: Universidad Tecnológica Nacional – TUP
Año lectivo: 2026

Integrantes del equipo
Rol	Nombre	Responsabilidad
P1 – Líder	Hugo	Repositorio, estructura y README
P2 – Desarrollador	Paco	Script de análisis y dataset
P3 – Revisor QA	Luis	Peer review y merge del PR
Escenario elegido
Escenario B – Análisis de Ventas de una Pequeña Empresa.

Dataset
Archivo: datos/ventas.csv. Dataset simulado de ventas 2024 con columnas: id, fecha, producto, cantidad, precio_unitario.

Resultados generados
resultados/resumen_mensual.csv – ventas por mes
resultados/grafico_ventas.png – evolución de ventas
Cómo ejecutar el script
Requisitos
Python 3.8+
pandas
matplotlib
Instalación de dependencias
pip install pandas matplotlib
Ejecución local
cd scripts
python analisis_ventas.py
Ejecución en Google Colab
!git clone https://github.com/ventricef012-ai/analisis-ventas-tup2026.git
%cd analisis-ventas-tup2026/scripts
!pip install pandas matplotlib
!python analisis_ventas.py
Trazabilidad Jira
Issue	Descripción
SCRUM-1	Estructura del repositorio
SCRUM-2	Script de análisis de ventas
SCRUM-3	Revisión QA y documentación
