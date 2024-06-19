/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      // backgroundImage: theme => ({
      //   'hero-pattern': "url('/public/images/background.jpg')",
      // }),
      colors: {
        'bg-purple' : '#B9C4F1',
      }
    },
  },
  plugins: [],
}

