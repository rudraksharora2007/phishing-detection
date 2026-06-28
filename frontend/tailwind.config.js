/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        cyber: {
          bg: "#050816",
          card: "#0b1226",
          neon: "#00f5d4",
          danger: "#ff4d6d",
          warn: "#ffb703",
          safe: "#2dd4bf"
        }
      },
      boxShadow: {
        glass: "0 8px 32px rgba(0, 245, 212, 0.15)"
      }
    }
  },
  plugins: []
};
