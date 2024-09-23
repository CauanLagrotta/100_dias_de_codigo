import { data } from "./data.js";

const container = document.querySelector(".container");

data.forEach((item, index) => {
  // Criando o card
  const card = document.createElement("div");
  card.classList.add("card");

  const cardInner = document.createElement("div");
  cardInner.classList.add("card-inner");

 
  const cardFront = document.createElement("div");
  cardFront.classList.add("card-content", "card-front");

  const title = document.createElement("h1");
  title.classList.add("title");
  title.innerHTML = item.title;

  const source = document.createElement("i");
  source.classList.add("source");
  source.innerHTML = item.source;

  const learnmore = document.createElement("p");
  learnmore.classList.add("learnmore");
  learnmore.innerHTML = item.learnmore;

  cardFront.appendChild(title);
  cardFront.appendChild(source);
  cardFront.appendChild(learnmore);

  // Criando a parte de tras
  const cardBack = document.createElement("div");
  cardBack.classList.add("card-content", "card-back");

  const description = document.createElement("p");
  description.classList.add("description");
  description.innerHTML = item.description;

  const back = document.createElement("p");
  back.classList.add("back");
  back.innerHTML = item.back;

  cardBack.appendChild(description);
  cardBack.appendChild(back);

  
  cardInner.appendChild(cardFront);
  cardInner.appendChild(cardBack);
  card.appendChild(cardInner);

  container.appendChild(card);

  // Eventos de clique
  learnmore.addEventListener("click", () => {
    card.classList.add("flip");
  });

  back.addEventListener("click", () => {
    card.classList.remove("flip");
  });
});
