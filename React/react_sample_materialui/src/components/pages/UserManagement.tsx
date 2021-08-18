// ユーザー管理ページのコンポーネント
import { memo, VFC, useEffect, useCallback } from "react";
import UserCard from "../organisms/user/UserCard";
import { useAllUsers } from "../../hooks/useAllUsers";



/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const UserManagement: VFC = memo(() => {
    // ユーザー情報取得用
    const { getUsers, loading, users } = useAllUsers();

    // 初期処理
    // ユーザー情報を取得する
    // eslint-disable-next-line
    useEffect(() => getUsers(), []);


    // props として渡す関数は都度再作成するとレンダリングの効率が悪いためメモ化する
    const onClickUser = useCallback((id: number) => {
        alert();
    }, [users]);

    return (
        <>
            {users.map((user) => (
                <UserCard
                    userName={user.username}
                    fullName={user.name}
                    // 画像は unsplash からランダムに取得する
                    imageUrl="https://source.unsplash.com/random"
                />
            ))}
        </>
    )
});