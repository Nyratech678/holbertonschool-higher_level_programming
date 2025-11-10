fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Erreur HTTP, statut : ' + response.status);
    }
    return response.json();
  })
  .then(data => {
    const characterName = document.getElementById('character');
    characterName.textContent = data.name;
  })
  .catch(error => {
    console.error('Erreur lors de la récupération des données :', error);
  });
