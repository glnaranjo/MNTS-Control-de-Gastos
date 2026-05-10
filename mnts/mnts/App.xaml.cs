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

            window.Width = 1500;
            window.Height = 900;

            window.MinimumWidth = 1500;
            window.MinimumHeight = 900;

            return window;
        }
    }
}