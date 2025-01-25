import React, { useContext } from "react";
import { Context } from "../store/appContext.js";


export const ContactList = () => {
  const { store, actions } = useContext(Context);
 
  return (
    <div className="container">
      <ul className="text-center">
        {store.contacts && store.contacts.length > 0 ? (
          store.contacts.map((contact) => (
            <li key={contact.id}>
              <strong>{contact.name}</strong>
              <br />
              {contact.email}
              <br />
              {contact.phone}
              <br />
              {contact.address}
              <span onClick={actions.addContact}> <i  class="fa-solid fa-address-book"></i>  </span>
              <span onClick={() => actions.deleteContact(contact.id)}><i  class="fa-solid fa-trash"></i></span>
              
            </li>
          ))
        ) : (
          <li>No contacts found</li>
        )}
      </ul>
    </div>
  );
};
