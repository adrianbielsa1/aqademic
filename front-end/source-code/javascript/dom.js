// The "DOM" module is meant to ease interaction with DOM elements.

export const searchInput = {
    element: document.getElementById("searchBarInput"),

    onKeyUp: function(event) {},
};

export const searchIcon = {
    element: document.getElementById("searchBarIcon"),

    onClick: function(event) {},
};

// Hook events so the elements know when they're clicked (or some other
// action is performed on them).
searchInput.element.addEventListener("keyup", searchInput.onKeyUp);
searchIcon.element.addEventListener("click", searchIcon.onClick);

Object.freeze(searchInput);
Object.freeze(searchIcon);
