namespace mnts
{
    public partial class App : Application
    {
        public App()
        {
            InitializeComponent();
        }

        protected override Window CreateWindow(IActivationState? activationState)
        {
            var window = new Window(new MainPage())
            {
                Title = "MNTS Control de gastos"
            };

#if WINDOWS
            // Proporción de pantalla móvil para pruebas en escritorio
            window.Width = 430;
            window.Height = 880;

            window.MinimumWidth = 360;
            window.MinimumHeight = 600;
#endif

            return window;
        }
    }
}
