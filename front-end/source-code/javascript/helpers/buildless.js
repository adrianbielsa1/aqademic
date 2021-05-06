// This module simply wraps the Buildless package into an object to make its
// usage in other files both easier and cleaner. Buidless provides Preact,
// HTM, and several tools more that aim to remove the compilation step.

import { render, html } from "https://unpkg.com/@fordi-org/buildless";

export const buildless = {
    render: render,
    html: html,
};
