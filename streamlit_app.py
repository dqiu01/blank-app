import streamlit as st

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [' '] * 9
    st.session_state.current_player = 'X'

# Function to check winner
def check_winner(board):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    return None

# Display game board
st.title("Tic-Tac-Toe")
st.write("Current Player:", st.session_state.current_player)

for i in range(3):  # Loop over rows
    cols = st.columns([1,1,1])  # Create 3 columns for the grid
    for j in range(3):  # Loop over columns
        idx = i * 3 + j  # Calculate the index of the cell
        with cols[j]:  # Place the button in the correct column
            if st.button(
                st.session_state.board[idx] if st.session_state.board[idx] != ' ' else " ",
                key=f"button_{i}_{j}"  # Use row and column indices to create a unique key
            ):
                if st.session_state.board[idx] == ' ':
                    # Update the board and check for a winner
                    st.session_state.board[idx] = st.session_state.current_player
                    winner = check_winner(st.session_state.board)
                    if winner:
                        st.success(f"Player {winner} wins!")
                        st.session_state.board = [' '] * 9  # Reset board
                    else:
                        # Switch to the next player
                        st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Reset button
if st.button("Reset Game"):
    st.session_state.board = [' '] * 9
    st.session_state.current_player = 'X'
