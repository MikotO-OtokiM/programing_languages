import { createContext, Dispatch, ReactNode, SetStateAction, useState } from "react";
import { User } from "../types/api/user";

// 管理者かどうかのフラグを User 型に追加
type LoginUser = User & { isAdmin: boolean };

export type LoginUserContextType = {
  loginUser: LoginUser | null;
  setLonginUser: Dispatch<SetStateAction<LoginUser | null>>
}

// Context で保持する内容を定義
export const LoginUserContext = createContext<LoginUserContextType>(
  // 初期値の型は as で強制的に LoginUserContextType とする
  {} as LoginUserContextType
);

export const LoginUserProvider = (props: { children: ReactNode }) => {
  const { children } = props;
  //　グローバルで利用したい値の State を定義
  const [loginUser, setLonginUser] = useState<LoginUser | null>(null);

  console.log(loginUser);

  return (
    // グローバルで利用したい値を value でオブジェクトとして渡す
    <LoginUserContext.Provider value={{ loginUser, setLonginUser }}>
      {children}
    </LoginUserContext.Provider>
  )
}
