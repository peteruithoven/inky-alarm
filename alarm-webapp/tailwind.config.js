const colors = require("tailwindcss/colors");

module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        enabled: colors.blue["400"]
      }
    }
  },
  variants: {
    extend: {
      borderRadius: ["first", "last"],
      borderWidth: ["first", "last"]
    }
  },
  plugins: []
};
