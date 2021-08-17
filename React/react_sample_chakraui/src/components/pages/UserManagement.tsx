// ユーザー管理ページのコンポーネント
import { memo, VFC, useEffect, useCallback } from "react";
import { Center, Spinner, useDisclosure, Wrap, WrapItem } from "@chakra-ui/react";

import { UserCard } from "../organisms/user/UserCard";
import { UserDetailModal } from "../organisms/user/UserDetailModal";
import { useAllUsers } from "../../hooks/useAllUsers";
import { useLoginUser } from "../../hooks/useLoginUser";
import { useSelectUser } from "../../hooks/useSelectUser";

/**
 * 関数コンポーネントであるため、型は VFC
 * コンポーネント全体をメモ化（メモリ展開）し、コンポーネントに渡された props が
 * 変更された時のみ再レンダリングするようにする
 */
export const UserManagement: VFC = memo(() => {
  // カスタムフック
  // Context のログインユーザ情報を利用するカスタムフック
  const { loginUser } = useLoginUser();
  // ユーザー情報取得用
  const { getUsers, loading, users } = useAllUsers();
  // 選択したユーザー情報のモーダル表示用
  const { onSelectUser, selectedUser } = useSelectUser();

  // 初期処理
  // ユーザー情報を取得する
  // eslint-disable-next-line
  useEffect(() => getUsers(), []);

  // モーダル表示
  // モーダルの動きは useDisclosure で制御
  const { isOpen, onOpen, onClose } = useDisclosure();
  // props として渡す関数は都度再作成するとレンダリングの効率が悪いためメモ化する
  const onClickUser = useCallback((id: number) => {
    onSelectUser({ id, users, onOpen });
  }, [users, onSelectUser, onOpen]);

  return (
    <>
      {/* ユーザーデータ取得中はスピナーを表示 */}
      {loading ? (
        <Center h="100vh">
          <Spinner />
        </Center>
      ) : (
        <Wrap p={{ base: 4, md: 10 }}>
          {users.map((user) => (
            // mx="auto"（中心寄せ表示）が効かない
            <WrapItem key={user.id} mx="auto">
              <UserCard
                id={user.id}
                // 画像は unsplash からランダムに取得する
                imageUrl="https://source.unsplash.com/random"
                userName={user.username}
                fullName={user.name}
                onClick={onClickUser}
              />
            </WrapItem>
          ))}
        </Wrap>
      )}
      <UserDetailModal
        user={selectedUser}
        isOpen={isOpen}
        isAdmin={loginUser?.isAdmin}
        onClose={onClose}
      />
    </>
  );
});