let rec load_input (ic:in_channel) (lst: int list) : int list =
  try
    let line = (input_line ic) in
    (load_input ic ((int_of_string line)::lst))
  with e ->
    lst

let rec zip (lst1: 'a list) (lst2: 'b list) : ('a*'b) list =
  (match lst1, lst2 with
   | x::xs, y::ys -> (x,y)::(zip xs ys)
   | _, _ -> [])


let rec zip3 (lst1: 'a list) (lst2: 'b list) (lst3: 'c list): ('a*'b*'c) list =
  (match lst1, lst2, lst3 with
   | x::xs, y::ys, z::zs -> (x,y,z)::(zip3 xs ys zs)
   | _, _, _ -> []
  )
let format_lst (lst: int list) : (int*int) list =
  (match lst with
   | x::xs -> (zip lst xs)
   | [] -> [])

let format_sliding_window (lst: int list) : (int*int*int) list =
  (match lst with
   | x::xs -> (match xs with
               | y::ys -> (zip3 lst xs ys)
               | [] -> [])
   | [] -> [])

let count_diff (lst: (int*int) list) : int =
  (List.fold_right (fun (prev, cur) acc -> if cur > prev then acc else acc+1) lst 0)

let count_inc (lst: (int*int) list) : int =
  (List.fold_right (fun (prev, cur) acc -> if cur > prev then acc+1 else acc) lst 0)


let solution1 (file_name: string) : int =
  let ic = open_in file_name in
  let lst = (format_lst (load_input ic [])) in
  (count_diff lst)

let solution2 (file_name: string) : int =
  let ic = open_in file_name in
  let windows = (format_sliding_window (load_input ic [])) in
  (count_inc (format_lst (List.rev (List.map (fun (a,b,c) -> a+b+c) windows))))
