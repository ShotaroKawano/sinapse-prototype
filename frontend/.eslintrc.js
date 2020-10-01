// https://eslint.org/docs/user-guide/configuring

module.exports = {
  root: true,
  parserOptions: {
    parser: "babel-eslint"
  },
  env: {
    browser: true
  },
  extends: [
    // https://github.com/vuejs/eslint-plugin-vue#priority-a-essential-error-prevention
    // consider switching to `plugin:vue/strongly-recommended` or `plugin:vue/recommended` for stricter rules.
    "plugin:vue/essential",
    // https://github.com/standard/standard/blob/master/docs/RULES-en.md
    "standard",

    // じん追記: エラー 'Vue' is not defined を消したい
    "vue",
    -"plugin:vue/recommended"
  ],
  // required to lint *.vue files
  plugins: ["vue"],
  // add your custom rules here
  rules: {
    // allow async-await
    "generator-star-spacing": "off",
    // allow debugger during development
    "no-debugger": process.env.NODE_ENV === "production" ? "error" : "off",
    indent: "off",
    "comma-dangle": "off",
    semi: "off",
    "dot-location": "off",
    "space-before-function-paren": "off",
    quotes: "off",
    "key-spacing": "off",
    "one-var": "off",
    "no-trailing-spaces": "off"
  },
  // じん追記: エラー 'Vue' is not defined を消したい
  globals: {
    Vue: true
  }
};
