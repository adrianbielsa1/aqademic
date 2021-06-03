import {} from "./helpers/request.js"; // This is needed so "request.js"'s body is executed.
import { getSearchResultListElement } from "./helpers/dom.js";
import { buildless } from "./helpers/buildless.js";
import { ResultList } from "./components/result-list.js";

// Called whenever a request is resolved.
document.addEventListener("customResolvedRequest", (event) => {
    // Extract the request's response.
    const response = event.detail;

    // Where we'll render the `ResultList` component.
    const domResultList = getSearchResultListElement();

    // Construct the `ResultList` component and render it.
    buildless.render(buildless.html`
        <${ ResultList } results=${ response }/>
    `, domResultList);
});
