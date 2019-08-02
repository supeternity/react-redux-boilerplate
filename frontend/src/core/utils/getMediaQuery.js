// req = {
//  * device:       string: see the switch section cases,
//  * orientation:  string: 'p' || 'l' || 'portrait' || 'landscape'
//    if orientation is false, created 'Portrait and Landscape' query
//  * style:        string: easy css for device
// }

import { css } from "styled-components";

export default function adaptive(req) {
  if (typeof req === "object" && req !== null) {
    if (req.orientation === "p" || req.orientation === "portrait") {
      req.orientation = "portrait";
    } else if (req.orientation === "l" || req.orientation === "landscape") {
      req.orientation = "landscape";
    }
    switch (req.device) {
      case "iPhone4":
        return css`
          @media only screen
            and (min-device-width: 320px)
            and (max-device-width: 480px)
            and (-webkit-min-device-pixel-ratio: 2)
            ${() => {
              return req.orientation
                ? `and (orientation: ${req.orientation})`
                : ``;
            }} {
            ${req.style}
          }
        `;
      case "iPhone5":
        return css`
          @media only screen
            and (min-device-width: 320px)
            and (max-device-width: 568px)
            and (-webkit-min-device-pixel-ratio: 2)
            ${() => {
              return req.orientation
                ? `and (orientation: ${req.orientation})`
                : ``;
            }} {
            ${req.style}
          }
        `;
      case "iPhone678":
        return css`
          @media only screen
            and (min-device-width: 375px)
            and (max-device-width: 667px)
            and (-webkit-min-device-pixel-ratio: 2)
            ${() => {
              return req.orientation
                ? `and (orientation: ${req.orientation})`
                : ``;
            }} {
            ${req.style}
          }
        `;
      case "iPhone678plus":
        return css`
          @media only screen
            and (min-device-width: 414px)
            and (max-device-width: 736px)
            and (-webkit-min-device-pixel-ratio: 3)
            ${() => {
              return req.orientation
                ? `and (orientation: ${req.orientation})`
                : ``;
            }} {
            ${req.style}
          }
        `;
      case "iPhoneX":
        return css`
          @media only screen
            and (min-device-width: 375px)
            and (max-device-width: 812px)
            and (-webkit-min-device-pixel-ratio: 3)
            ${() => {
              return req.orientation
                ? `and (orientation: ${req.orientation})`
                : ``;
            }} {
            ${req.style}
          }
        `;
      default:
        return ``;
    }
  } else {
    console.error(
      `Media queries creater expected Object, but received ${typeof req}`
    );
  }
}
