# MNTS: Control de Gastos

> Aplicación de escritorio para el control de gastos personales.

MNTS es una reescritura moderna de una herramienta de control de gastos originalmente construida en Python/Tkinter. Esta versión está desarrollada en **.NET MAUI Blazor Hybrid**, con almacenamiento 100% local — ningún dato del usuario sale de su dispositivo.

## Índice

- [Características](#características)
- [Stack tecnológico](#stack-tecnológico)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Almacenamiento de datos](#almacenamiento-de-datos)
- 
## Características

- **Registro de gastos** por categoría, con fecha y monto.
- **Registro de ingresos/presupuesto** mensual.
- **Categorías personalizables**: nombre e ícono editables por el usuario, con restauración a valores por defecto.
- **Resumen mensual** con:
  - Gráfico de torta/dona por categoría.
  - Gráfico de línea con evolución del gasto en los últimos 6 meses.
  - Comparación automática contra el mes anterior.
  - Estadísticas de día con mayor/menor gasto.
- **Exportación a Excel** (`.xlsx`) del resumen mensual.
- **Edición y eliminación individual** de registros (gastos e ingresos), con listado filtrable por fecha.
- **Reinicio total de datos**, protegido con confirmación por frase de texto.
- Diseño responsive pensado para uso en PC/notebook (no para dispositivos móviles).

## Stack tecnológico

| Área | Tecnología |
|---|---|
| Framework | .NET MAUI Blazor Hybrid |
| Lenguaje | C# / Razor |
| Base de datos | SQLite (`sqlite-net-pcl`) |
| Gráficos | Blazor-ApexCharts |
| Exportación a Excel | ClosedXML |
| Estilos | CSS aislado por componente (scoped CSS de Blazor) |

## Estructura del proyecto

```
mnts/
├── Components/
│   └── Pages/          # Páginas .razor (Gastos, Ingresos, Resumen, etc.)
├── Models/              # Entidades: Gasto, Ingreso, Etiqueta, etc.
├── Services/
│   ├── GastosService.cs   # Acceso a datos (SQLite)
│   └── ExportService.cs   # Generación de archivos Excel
├── Resources/
│   └── Raw/             # Assets embebidos (manual de uso en PDF)
├── wwwroot/              # Imágenes y assets estáticos
└── MauiProgram.cs        # Configuración e inyección de dependencias
```

## Almacenamiento de datos

MNTS **no envía ningún dato a servidores externos**. Toda la información (gastos, ingresos, categorías personalizadas) se guarda en una base SQLite local, ubicada en el directorio de datos de la aplicación en el dispositivo del usuario.

Los archivos exportados a Excel se generan localmente y se abren con el programa predeterminado del sistema para archivos `.xlsx`.
---

*MNTS: Control de Gastos es software gratuito, pensado para ayudar a los usuarios en su día a día.*
