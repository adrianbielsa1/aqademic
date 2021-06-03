// This module prepares event listeners and fires requests to the server
// when appropriate.

import {
    getSearchInputElement, dispatchResolvedRequestEvent, dispatchRejectedRequestEvent
} from "./dom.js";

document.addEventListener("customStartRequest", (e) => {
    // Remove spaces from both ends of the string, then, replace multiple
    // spaces with a single dash.
    const query = getSearchInputElement().value.trim().replace(/ +/g, "-");

    // Ignore empty requests.
    if (query == "") { return; }

    const api = {
        host: "127.0.0.1",
        port: 8000,
        version: 1,

        target: "students",

        // When the input is numeric we query by file number, otherwise, we search
        // using the students' names.
        method: isNaN(query) ? "by-names" : "by-file",
    };

    const url = `http://${api.host}:${api.port}/${api.target}/api/v${api.version}/${api.method}/${query}/`;

    const request = fetch(url, {
        mode: "cors",
        headers: {
            "Access-Control-Request-Method": "GET",
        },
    });

    request.then(
        response => response.json(), // Builds a Javascript object from the response's body.
        reason => dispatchRejectedRequestEvent(reason)
    ).then(
        response => dispatchResolvedRequestEvent(response),
        reason => dispatchRejectedRequestEvent(reason) // TODO: Is this second call needed?
    );
});
