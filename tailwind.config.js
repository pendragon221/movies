/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    './templates/**/*.html',
    './**/templates/**/*.html'
  ],
  theme: {
    fontFamily: {
      'default': ['"Open Sans"', 'sans-serif'],
    },
    extend: {},
  },
  plugins: [],
}

