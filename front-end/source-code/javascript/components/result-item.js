import { buildless } from "./../helpers/buildless.js";

export const ResultItem = function ({ names, file }) {
    return buildless.html`
        <div class="item">
            <div class="names">Names: ${ names }</div>
            <div class="file">File: ${ file }</div>
        </div>
    `;
};
