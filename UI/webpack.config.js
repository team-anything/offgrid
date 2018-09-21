var path = require("path");

module.exports = {
  watch: true,
  entry: "./main.js",
  output: {
    path: path.resolve(__dirname, "../Web/digital/static/js"),
    filename: "bundle.js",
    publicPath: "/dist"
  },
  module: {
    rules: [
      {
        test: [/\.scss$/,/\.sass$/],
        use: [
          {
            loader: "style-loader" // creates style nodes from JS strings
          },
          {
            loader: "css-loader" // translates CSS into CommonJS
          },
          {
            loader: "sass-loader" // compiles Sass to CSS
          }
        ]
      },
{
    test: /\.css$/,
    loader: 'style-loader!css-loader'
}
    ]
  }
};