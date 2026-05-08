module.exports = {
  content: [
    '../templates/**/*.html',
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('daisyui'),  // ← 追加
  ],
  daisyui: {
    themes: ["light", "dark", "cupcake"],  // 使用するテーマを指定
  },
}