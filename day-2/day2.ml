exception InvalidDirection of string
type direction = U | D | R

let direction_of_string (x: string) : direction =
  (match x with
   | "forward" -> R
   | "up" -> U
   | "down" -> D
   | _ -> raise (InvalidDirection "Input string is not a valid direction")
  )

let rec load_input (ic:in_channel) (lst: (direction*int) list) : (direction*int) list =
  try
    let line = (String.split_on_char ' ' (input_line ic)) in
    (match line with
    | x::y::[] -> (load_input ic (((direction_of_string x), (int_of_string y))::lst))
    | _ -> [])
  with e -> lst

let move_ship (movement: (direction*int)) (position: int*int) =
  let x, y = position in
  (match movement with
   | (U, d) -> (x, y-d)
   | (D, d) -> (x, y+d)
   | (R, d) -> (x+d, y))

let compute_depth (movements: (direction*int) list) : int*int =
  (List.fold_right move_ship movements (0, 0))

let solution1 (file_name: string) : int =
  let movements = (load_input (open_in file_name) []) in
  let (x, y) = (compute_depth movements) in
  x*y

let move_ship2 (movement: (direction*int)) (position: (int*int*int)) =
  let x, y, aim = position in
  (match movement with
   | (U, d) -> (x, y, aim-d)
   | (D, d) -> (x, y, aim+d)
   | (R, d) -> (x+d, y+(d*aim), aim))

let solution2 (file_name: string) : int =
  let movements = (load_input (open_in file_name) []) in
  let (x, y, aim) = (List.fold_right move_ship2 movements (0, 0, 0)) in
  x*y
