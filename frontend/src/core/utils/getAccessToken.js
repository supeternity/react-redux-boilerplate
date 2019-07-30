import { getCookie } from "./cookie";
import { USER_TOKEN } from "./cookie/types"

export default function() {
  return getCookie(USER_TOKEN)
}