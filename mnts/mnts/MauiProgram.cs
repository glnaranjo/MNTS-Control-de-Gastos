using Microsoft.Extensions.Logging;
using ApexCharts;

namespace mnts
{
    public static class MauiProgram
    {
        public static MauiApp CreateMauiApp()
        {
            var builder = MauiApp.CreateBuilder();
            builder
                .UseMauiApp<App>()
                .ConfigureFonts(fonts =>
                {
                    fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
                });

            builder.Services.AddMauiBlazorWebView();

#if ANDROID
            // Fija el TextZoom al 100% en Android para evitar que el ajuste de fuente
            // del sistema (ej: fuentes grandes en configuración del celular) rompa el layout
            Microsoft.AspNetCore.Components.WebView.Maui.BlazorWebViewHandler.BlazorWebViewMapper.AppendToMapping("PreventSystemFontScaling", (handler, view) =>
            {
                handler.PlatformView.Settings.TextZoom = 100;
            });
#endif

            builder.Services.AddSingleton<Services.GastosService>();

            builder.Services.AddApexCharts();

            builder.Services.AddSingleton<Services.ExportService>();

#if DEBUG
            builder.Services.AddBlazorWebViewDeveloperTools();
    		builder.Logging.AddDebug();
#endif

            return builder.Build();
        }
    }
}
