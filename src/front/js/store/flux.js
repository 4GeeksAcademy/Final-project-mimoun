const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			contacts: [],
			baseURLcontact: 'https://playground.4geeks.com/contact',
			user: 'mimoun'
		},
		actions: {
			setContacts: (data) => { setStore({ contacts: data.contacts }); },
			exampleFunction: () => { getActions().changeColor(0, "green"); },
			getMessage: async () => {
				try {
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				} catch (error) {
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore()
				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});
				//reset the global store
				setStore({ demo: demo });
			},
			addContact: async (dataToSend) => {
				const uri = `${getStore().baseURLcontact}/agendas/${getStore().user}`
				const options = {
					method: 'POST',
					headers: {
						"Content-Type": "application/json"
					},
					body: JSON.stringify(dataToSend)
				}
				const response = await fetch(uri, options);
				if (!response.ok)
					console.log('error:', response.status, response.statusText)
				return
			},
			deleteContact: async (contact) => {
				const uri = `${getStore().baseURLcontact}/agendas/${getStore().user}/${contact.id}`
				const options = {
					method: 'DELETE'
				}
				const response = await fetch(uri, options);
				if (!response.ok) {
					console.log('error:', response.status, response.statusText)
					return
				}
				getActions().getContacts();
			},
			getContacts: async () => {
				const uri = `${getStore().baseURLcontact}/agendas/${getStore().user}`;
				const options = {
					method: "GET"
				};
				const response = await fetch(uri, options);
				if (!response.ok) {
					console.error("Error:", response.status, response.statusText);
					return;
				}
				const data = await response.json();
				getActions().setContacts(data);
			}
		}
	};
};

export default getState;
