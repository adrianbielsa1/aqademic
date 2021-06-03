import { buildless } from "./../helpers/buildless.js";
import { ResultItem } from "./result-item.js";

export const ResultList = function ({ results }) {
    // The JSON `results` transformed into HTML.
    const results_as_htmls = [];

    // TODO: Maybe it would be better to use `map`.
    for (const result of results) {
        results_as_htmls.push(
            buildless.html`
                <${ ResultItem }
                    names=${ result.names }
                    file=${ result.file }
                />
            `
        );
    }

    return buildless.html`${ results_as_htmls }`;
};
