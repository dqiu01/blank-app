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

# Add custom CSS for responsive grid layout
st.markdown(
    """
    <style>
    /* Main container adjustments for responsiveness */
    div.block-container {
        padding: 1rem;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 600px; /* Prevent grid from stretching too wide */
    }

    /* Button styling for Tic-Tac-Toe grid */
    div.stButton > button {
        height: auto;
        width: 100%; /* Ensure buttons stretch to column width */
        aspect-ratio: 1; /* Maintain square buttons */
        font-size: 1.2rem; /* Increase font size */
        margin: 5px; /* Add spacing between buttons */
    }

    /* Adjust Reset button to fit content */
    div.stButton > button:contains("Reset Game") {
        font-size: 1rem;
        padding: 10px 20px;
    }

    /* Columns styling to center content */
    div[data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display game board
st.title("Tic-Tac-Toe")
st.write(f"Current Player: {st.session_state.current_player}")

# Render the game board
with st.container():
    for i in range(3):  # Loop over rows
        cols = st.columns([1, 0.1, 1, 0.1, 1])  # Equal-width columns
        for j in range(3):  # Loop over columns
            idx = i * 3 + j
            with cols[j]:
                if st.button(
                    st.session_state.board[idx] if st.session_state.board[idx] != ' ' else " ",
                    key=f"button_{i}_{j}"  # Unique key for each button
                ):
                    if st.session_state.board[idx] == ' ':
                        st.session_state.board[idx] = st.session_state.current_player
                        winner = check_winner(st.session_state.board)
                        if winner:
                            st.success(f"Player {winner} wins!")
                            st.session_state.board = [' '] * 9  # Reset board
                        else:
                            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Reset button
if st.button("Reset Game"):
    st.session_state.board = [' '] * 9
    st.session_state.current_player = 'X'
