fetch ('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then(response => response.json())
  .then(data => {
    const helloDiv = document.getElementById('hello');
    helloDiv.textContent = data.hello;
  })
  .catch(error => {
    console.error('Erreur lors de la récupération des données :', error);
  });
