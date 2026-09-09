module.exports = {
  darkMode: 'class',
  content: ['./低温设备使用手册.html'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          500: '#0284c7',
          600: '#0369a1',
          700: '#075985',
          800: '#0c4a6e',
          900: '#082f49'
        },
        accent: {
          50: '#fff7ed',
          500: '#f97316',
          600: '#ea580c'
        }
      },
      fontFamily: {
        sans: ['Microsoft YaHei', 'Noto Sans SC', 'Segoe UI', 'sans-serif'],
        mono: ['Cascadia Mono', 'Consolas', 'ui-monospace', 'monospace']
      }
    }
  },
  plugins: []
};
