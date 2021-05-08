// This module handles as much direct interaction with the DOM as possible,
// so other modules can interact with it through custom events or functions.

class DOMNotLoadedError extends Error {
    constructor(message) {
        super(message);
        this.name = "DOMNotLoadedError";
    }
}

export const getSearchInputElement = () => {
    if (document.readyState === "loading") {
        throw new DOMNotLoadedError("");
    }

    return document.querySelector(".page > .search > .query > .bar > .input");
};

export const getSearchButtonElement = () => {
    if (document.readyState === "loading") {
        throw new DOMNotLoadedError("");
    }

    return document.querySelector(".page > .search > .query > .bar > .button");
};

export const getSearchResultsElement = () => {
    if (document.readyState === "loading") {
        throw new DOMNotLoadedError("");
    }

    return document.querySelector(".page > .search > .result > .list");
};

// Gathers the current input query and dispatches an event containing
// said information so other objects can potentially transfer the request
// to the server.
const dispatchStartRequestEvent = function() {
    const input = getSearchInputElement();

    document.dispatchEvent(new CustomEvent("customStartRequest", { detail: input.value }));
}

export const dispatchUpdateResultsEvent = function(entries) {
    document.dispatchEvent(new CustomEvent("customUpdateResultsEvent", { detail: entries }));
}

const mount = function() {
    const input = getSearchInputElement();
    const button = getSearchButtonElement();

    input.addEventListener("keyup", (e) => {
        // TODO: It would be good to only dispatch an event when the length changes.
        // Currently, if you press ANY key (such as shift) and the input's length
        // exceeds the threshold, the event will be dispatched no matter what.
        //
        // NOTE: 13 is the code for the "ENTER" key.
        //
        // This checks for the length of the string written in the input field.
        if (input.value.length > 4) {
            dispatchStartRequestEvent();
        } else if (e.keyCode === 13) {
            dispatchStartRequestEvent();
        }
    });

    button.addEventListener("click", (e) => {
        dispatchStartRequestEvent();
    });
};

if (document.readyState !== "loading") {
    mount();
} else {
    document.addEventListener("DOMContentLoaded", () => {
        mount();
    });
}
