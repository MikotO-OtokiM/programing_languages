import { useContext } from "react";
import { LoginUserContext, LoginUserContextType, } from "../providers/LoginUserProvider";

// グローバルに保持した値は useContext にて利用できる
// どの Context かを示すために、作成した Context を引数で渡す
export const useLoginUser = (): LoginUserContextType => useContext(LoginUserContext)