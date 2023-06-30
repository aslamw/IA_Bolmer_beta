const puppeteer = require('puppeteer');

async function trocarAbas() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto('https://www.google.com'); // Abre a primeira página
  
  // Obtém a lista de páginas abertas
  //const pages = await browser.pages();

  // Fecha a página atual
  //await page.close();
  const teste = async () => {

  }


  // Faça o que for necessário com a nova página aberta

  //await browser.close();
}

trocarAbas();
