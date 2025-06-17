const arr = msg.payload;

const devices = {
  Sensor_Optico_Altura: "eff7e5ff-f872-4f10-a631-ae54ebd62d29",
  Esteira: "c8fc1615-b429-47bd-8293-911b534a232c",
  Sensor_Optico_Rampa1: "82845a6a-3981-4f20-93bd-884a59fc92e9",
  Sensor_Optico_Rampa2: "64fcf23d-861b-45f4-82b3-6a2774d75808",
  Sensor_Capacitivo: "070b84ea-331d-4c14-b8dc-41b84cc3cf10",
  Sensor_Indutivo: "920d24b2-7159-4595-a278-2809223d8de5",
  Sensor_Optico_Esteira: "f863331b-90d2-4f3c-809b-349cfd12c7cc",
  Atuador_A: "985c1c59-d52a-458a-80ae-f46435d5491a",
  Atuador_B: "b52eef9a-9a14-490f-9718-cdc5bb092d0c"
};

if (!Array.isArray(arr)) {
    return [null];  // Se não for array, não envia nada
}

const msgs = arr.slice(0, -1).map(o => {
    const originalName = o.item.displayName.text;
    const uuid = devices[originalName] || originalName; // Se não encontrado, usa o nome original

    return {
        payload: {
            device_id: uuid,
            state: o.item.value,
            timestamp: new Date().toISOString()
        }
    };
});

return [msgs];
