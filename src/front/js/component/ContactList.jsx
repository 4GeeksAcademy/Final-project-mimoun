import React, { useContext, useEffect } from "react";
import { Context } from "../store/appContext.js";

export const ContactList = () => {
  const { store, actions } = useContext(Context);
  const baseURL = "https://playground.4geeks.com/contact";
  const user = "mimoun";

  
  const getContacts = async () => {
    const uri = `${baseURL}/agendas/${user}`;
    const options = {
      method: "GET",
    };

    const response = await fetch(uri, options);

    if (!response.ok) {
      console.error("Error:", response.status, response.statusText);
      return;
    }

    const data = await response.json(); 
    actions.setContacts(data); 
  };

 
  useEffect(() => {
    getContacts();
  }, []);

  return (
    <div className="container">
      <ul>
        {store.contacts && store.contacts.length > 0 ? (
          store.contacts.map((contact, index) => (
            <li key={index}>
              <strong>{contact.name}</strong>
              <br />
              {contact.email}
              <br />
              {contact.phone}
              <br />
              {contact.adress}
            </li>
          ))
        ) : (
          <li>No contacts found</li>
        )}
      </ul>
    </div>
  );
};
