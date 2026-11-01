# MNTS: Control de Gastos (Versión 2.0 - Mobile Edition)

> Aplicación móvil (y multiplataforma) para el control ágil y privado de gastos personales.

MNTS es una aplicación desarrollada en **.NET MAUI Blazor Hybrid**, diseñada específicamente con enfoque **mobile-first** para teléfonos celulares, con almacenamiento 100% local — ningún dato del usuario sale de su dispositivo.

## Índice

- [Características](#características)
- [Novedades de la Versión 2.0](#novedades-de-la-versión-20)
- [Stack tecnológico](#stack-tecnológico)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Almacenamiento de datos](#almacenamiento-de-datos)

## Características

- **Registro de gastos mobile-friendly**: interfaz adaptada a una mano, con teclado numérico decimal nativo y fecha preseleccionada.
- **Registro de ingresos/presupuesto** mensual con panel táctil de carga rápida.
- **Categorías personalizables**: selector táctil de emojis y nombres editables, con opción de restauración de fábrica.
- **Resumen mensual interactivo**:
  - Métricas rápidas (Gasto total, Ingreso total y Balance).
  - Gráfico de torta/dona por categoría.
  - Gráfico de línea con evolución histórica (últimos 6 meses).
  - Comparación automática con el mes anterior y estadísticas clave.
- **Exportación a Excel** (`.xlsx`) compatible con el visor de archivos del teléfono.
- **Gestión individual de movimientos**: listado de gastos e ingresos con edición y eliminación directa.
- **Reinicio total de datos**, protegido con confirmación por frase de seguridad.
- **Privacidad absoluta**: sin servidores externos, sin tracking.

## Novedades de la Versión 2.0

- 📱 **Diseño 100% Mobile First**: Nueva interfaz con barra superior móvil (`Mobile TopBar`), botones inferiores fijos para el pulgar (`Sticky Bottom Actions`) y tarjetas táctiles optimizadas para celulares.
- 📐 **Safe Area Inset Support**: Adaptado para muescas (notch), barras de estado e indicadores de inicio de iOS y Android.
- ⌨️ **Teclados nativos optimizados**: Atributos `inputmode="decimal"` y soporte robusto para punto y coma decimal en todas las regiones.
- 🎨 **Paleta de diseño moderna**: Inspirada en aplicaciones fintech actuales (estilo Nubank/Revolut), con transiciones táctiles y feedback visual instantáneo.
- ⚡ **Carga instantánea de Resumen**: Visualización inmediata del mes en curso sin necesidad de clics previos.

## Stack tecnológico

| Área | Tecnología |
|---|---|
| Framework | .NET MAUI Blazor Hybrid (.NET 10) |
| Lenguaje | C# / Razor |
| Base de datos | SQLite (`sqlite-net-pcl`) local |
| Gráficos | Blazor-ApexCharts |
| Exportación a Excel | ClosedXML |
| Estilos | CSS aislado y Design System mobile-first |

## Estructura del proyecto

```
mnts/
├── Components/
│   ├── Layout/         # Layout principal
│   └── Pages/          # Pantallas móviles (Home, Gastos, Ingresos, Resumen, etc.)
├── Models/              # Entidades: Gasto, Ingreso, Etiqueta, etc.
├── Services/
│   ├── GastosService.cs   # Acceso a datos (SQLite)
│   └── ExportService.cs   # Generación de archivos Excel
├── Resources/
│   └── Raw/             # Assets embebidos (Manual de uso en PDF)
├── wwwroot/              # Imágenes, estilos globales y assets estáticos
└── MauiProgram.cs        # Configuración e inyección de dependencias
```

## Almacenamiento de datos

MNTS **no envía ningún dato a servidores externos**. Toda la información (gastos, ingresos, categorías personalizadas) se guarda en una base SQLite local en el dispositivo del usuario.

---

*MNTS: Control de Gastos es software gratuito de la iniciativa G-NAND, pensado para ayudar a los usuarios en su día a día.*
