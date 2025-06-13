const stored_quantity = 100;

const tipos = ["metalicas", "plasticas", "descarte"];

const ids = {
  metalicas: "9245c36b-96d9-474b-a227-80e85658f422",
  plasticas: "9bd68039-9827-4078-ac98-1b0a96505291",
  descarte: "3b403383-9a56-4b7e-bd78-c153105444cf"
};

function randomPartType() {
  return tipos[Math.floor(Math.random() * tipos.length)];
}

const tipo = randomPartType();

msg.payload = {
  part_id: ids[tipo],
  part_type: tipo,
  stored_quantity: stored_quantity
};

return msg;