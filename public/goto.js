
const resources = [
  "https://finviz.com/quote.ashx?t=",
  "https://atom.finance/quote/",
  "https://www.koyfin.com/charts/g/",
  "https://stocktwits.com/symbol/",
  "https://marketchameleon.com/Overview/"
];

window.onload = function() {
  const stock = new URLSearchParams(window.location.search).get("stock").toUpperCase();
  this.console.log(stock)
  for (const resource of resources) {
    this.console.log(resource + stock);
    window.open(resource + stock, "_blank");
  }
  window.open('', '_self').close(); // probably doesn't work, but worth a shot
};