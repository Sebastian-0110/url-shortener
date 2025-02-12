const API_PREFIX = import.meta.env.VITE_API_PREFIX;

const endpoint = (path) => `${API_PREFIX}${path}`;

export default endpoint;