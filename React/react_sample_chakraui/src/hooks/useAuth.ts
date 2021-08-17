/* eslint-disable react-hooks/exhaustive-deps */
// ユーザー認証用カスタムフック
import { useCallback, useState } from "react"
import { useHistory } from "react-router-dom";
import axios from "axios";

import { User } from "../types/api/user";
import { useLoginUser } from "./useLoginUser";
import { useMessage } from "./useMessage";

export const useAuth = () => {
  // State
  // ログイン認証の状態
  const [loading, setLoading] = useState(false)

  // カスタムフック
  // ログインユーザ情報を Context にセットするカスタムフック
  const { setLonginUser } = useLoginUser();
  // メッセージダイアログ表示のカスタムフック（認証結果の表示）
  const { showMessage } = useMessage();

  // 画面遷移用の History
  const history = useHistory();

  const login = useCallback(
    // ユーザーID を利用し認証を実施
    (id: string) => {
      setLoading(true);
      // サンプルとして JSONPlaceholder を利用する
      // 正常にデータ取得できた場合の処理は then で記載記載する
      axios.get<User>(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then((res) => {
          // ユーザーID のデータが存在する場合
          if (res.data) {
            // id が 10 のユーザーを管理者とする
            const isAdmin = res.data.id === 10 ? true : false;
            // 取得したユーザーデータをスプレッド構文で展開し isAdmin を追加して
            // Context のログインユーザ情報を設定
            setLonginUser({ ...res.data, isAdmin });
            // HOME 画面へ遷移
            history.push("/home");
            showMessage({ title: "ログインしました", status: "success" });
          } else {
            showMessage({ title: "ユーザーが見つかりません", status: "error" });
            setLoading(false);
          }
        }).catch(() => {
          showMessage({ title: "ログインできません", status: "error" })
          setLoading(false);
        }
        )
    },
    [history, showMessage, setLonginUser]
  )
  // 認証結果と認証状態を戻す
  return { login, loading };
};