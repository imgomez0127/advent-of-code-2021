let rec load_input (ic:in_channel) (lst: string list) : string list =
  try
    let line = (input_line ic) in
    (load_input ic (lst@[line]))
  with e ->
    lst

let paren_pairs = [
    ("(", ")");
    ("{", "}");
    ("[", "]");
    ("<", ">");
]

let paren_scores = [
    ("", 0);
    (")", 3);
    ("]", 57);
    ("}", 1197);
    (">", 25137)
]

let autocomplete_scores = [
    ("", 0);
    (")", 1);
    ("]", 2);
    ("}", 3);
    (">", 4)
]

let explode (s: string) : string list =
  let rec exp i l =
    if i < 0 then l else exp (i - 1) ((String.make 1 s.[i]) :: l) in
  exp (String.length s - 1) []

let rec is_balanced (stack: string list) (parens: string list) : bool*string list=
  (match parens, stack with
   | x::xs, y::ys when x = y -> (is_balanced ys xs)
   | x::xs, _ when (List.mem_assoc x paren_pairs) ->
      (is_balanced ((List.assoc x paren_pairs)::stack) xs)
   | [], _ -> (true, stack)
   | x::xs, _ -> (false, x::stack)
  )

let compute_score (result: bool*string list) =
  let balanced, stack = result in
  (match balanced, stack with
   | true, _ -> 0
   | false, x::xs -> (List.assoc x paren_scores)
   | false, [] -> 0)

let solution1 (file_name: string) =
  let chunks = List.map explode (load_input (open_in file_name)) in
  (List.fold_right
     (fun x acc -> (compute_score x)+acc)
     (List.map (is_balanced []) chunks)
     0)
