import axios from "axios";

export async function postRequest(endpoint, data, config) {
	console.log("postRequest called");

	let response, error;

	try {
		response = (await axios.post(endpoint, data, config)).data;
	}

	catch (err) {
		error = err;
	}
	
	return { response, error }
}
