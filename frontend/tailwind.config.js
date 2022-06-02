module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      'error-login' : {
        '0%, 100%': { 'backgroud-color': 'blue' },
        '50%': { 'backgroud-color': 'red' },
      }
    },
  },
  plugins: [
    function ({ addVariant }) {
        addVariant('child', '& > *');
        addVariant('child-hover', '& > *:hover');
    }
  ],
}
