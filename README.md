# Sistema de Gestión de Inventarios

 ![Fondo](https://cdn2.hubspot.net/hubfs/2283874/Fotos%20blog/inventario.jpg)

## Descripción

Este proyecto implementa un sistema de gestión de inventarios que permite registrar, administrar y consultar información relacionada con productos, categorías, proveedores y bodegas. El sistema facilita la gestión eficiente del stock y las relaciones entre las entidades involucradas.

## Funcionalidades

### Funcionales


1. **Registro de entidades**:
   * Registrar productos con nombre, descripción, precio, stock inicial y categoría.
   * Registrar categorías con nombre y descripción.
   * Registrar proveedores con nombre, dirección, teléfono y productos suministrados.
   * Registrar bodegas con nombre, ubicación, capacidad máxima y productos almacenados.
2. **Gestión de stock**:
   * Incrementar o retirar stock de productos existentes.
   * Calcular el valor total del inventario.
3. **Relaciones entre entidades**:
   * Asociar productos con categorías, proveedores y bodegas.
   * Verificar la capacidad de las bodegas antes de almacenar productos.
   * Consultar disponibilidad de productos en bodegas específicas.
4. **Consultas y reportes**:
   * Consultar información detallada de productos, categorías, proveedores y bodegas.
   * Generar reportes de stock total, por categoría, por proveedor y por bodega.
5. **Interfaz gráfica**:
   * Interactuar con el sistema a través de una interfaz gráfica amigable utilizando `tkinter`.
   * Mostrar mensajes de advertencia y confirmación con `messagebox`.

### No Funcionales


1. **Usabilidad**:
   * La interfaz debe ser intuitiva y accesible para usuarios sin conocimientos técnicos.
2. **Rendimiento**:
   * El sistema debe responder rápidamente incluso con un número razonable de registros.
3. **Portabilidad**:
   * El sistema debe ejecutarse en cualquier máquina con Python 3.8+ y `tkinter` instalado.
4. **Confiabilidad**:
   * Validar operaciones como capacidad de bodegas y disponibilidad de stock.
5. **Escalabilidad**:
   * Diseñado para facilitar futuras ampliaciones como soporte para bases de datos o más reportes.
6. **Compatibilidad**:
   * Compatible con sistemas operativos Windows, macOS y Linux.
7. **Mantenibilidad**:
   * Código modular para facilitar actualizaciones y extensiones.

# Instalación


1. Clona el Repositorio:

   Si estás utilizando Git, clona el repositorio a tu máquina local:

```bash
git clone  https://github.com/DanielChavezV/Parcial_Programacion_I.git
```


2. Crear y activar el entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```


3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

# Ejecución

Para ejecutar el proyecto, usa el siguiente comando:

```bash
python main.py
```

# Autor

**Daniel Steven Chavez Valdes y Juan Sebastian Castañeda**

**Ingeniería de Sistemas 4 Semestre** **Universidad Libre Seccional Cali**
